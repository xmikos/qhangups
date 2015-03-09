import logging, html

import hangups

logger = logging.getLogger(__name__)


def text_to_segments(text):
    """Create list of ChatMessageSegments from text"""
    # Replace two consecutive spaces with space and non-breakable space,
    # then split text to lines
    lines = text.replace('  ', ' \xa0').splitlines()
    if not lines:
        return []

    # Generate line segments
    segments = []
    for line in lines[:-1]:
        if line:
            segments.append(hangups.ChatMessageSegment(line))
        segments.append(hangups.ChatMessageSegment('\n', hangups.SegmentType.LINE_BREAK))
    if lines[-1]:
        segments.append(hangups.ChatMessageSegment(lines[-1]))

    return segments


def segment_to_html(segment):
    """Create simple HTML from ChatMessageSegment"""
    text = html.escape(segment.text)
    text = text.replace('\n', '<br>\n')

    message = []
    if segment.type_ == hangups.schemas.SegmentType.TEXT:
        message.append(text)
    elif segment.type_ == hangups.schemas.SegmentType.LINK:
        message.append(
            '<a href="{}">{}</a>'.format(segment.link_target if segment.link_target else text, text)
        )
    elif segment.type_ == hangups.schemas.SegmentType.LINE_BREAK:
        message.append('<br>\n')
    else:
        logger.warning('Ignoring unknown chat message segment type: {}'.format(segment.type_))

    if not segment.type_ == hangups.schemas.SegmentType.LINE_BREAK:
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
