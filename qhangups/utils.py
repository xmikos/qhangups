import logging, html

import hangups

logger = logging.getLogger(__name__)


def text_to_segments(text):
    """Create list of ChatMessageSegments from text"""
    return hangups.ChatMessageSegment.from_str(text)


def segment_to_html(segment):
    """Create simple HTML from ChatMessageSegment"""
    text = html.escape(segment.text) if segment.text else ""
    text = text.replace('\n', '<br>\n')

    message = []
    if segment.type_ == hangups.hangouts_pb2.SEGMENT_TYPE_TEXT:
        message.append(text)
    elif segment.type_ == hangups.hangouts_pb2.SEGMENT_TYPE_LINK:
        message.append(
            '<a href="{}">{}</a>'.format(segment.link_target if segment.link_target else text, text)
        )
    elif segment.type_ == hangups.hangouts_pb2.SEGMENT_TYPE_LINE_BREAK:
        message.append('<br>\n')
    else:
        logger.warning('Ignoring unknown chat message segment type: {}'.format(segment.type_))

    if not segment.type_ == hangups.hangouts_pb2.SEGMENT_TYPE_LINE_BREAK:
        for is_f, f in ((segment.is_bold, 'b'), (segment.is_italic, 'i'),
                        (segment.is_strikethrough, 's'), (segment.is_underline, 'u')):
            if is_f:
                message.insert(0, '<{}>'.format(f))
                message.append('</{}>'.format(f))

    return ''.join(message)


def message_to_html(conv_event):
    """Create simple HTML from ChatMessageEvent"""
    lines = [segment_to_html(segment) for segment in conv_event.segments]
    attachments = ['<a href="{}">{}</a>'.format(url, url) for url in conv_event.attachments]

    html = ["".join(lines)]
    html.extend(attachments)

    return '<br>\n'.join(html)
