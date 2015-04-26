# Maintainer: Michal Krenek (Mikos) <m.krenek@gmail.com>
pkgname=qhangups
pkgver=1.5.2
pkgrel=1
pkgdesc="Alternative client for Google Hangouts written in PyQt"
arch=('any')
url="https://github.com/xmikos/qhangups"
license=('GPL3')
depends=('hangups-git' 'python-quamash' 'python-pyqt4' 'python-appdirs')
makedepends=('python-setuptools')
source=(https://github.com/xmikos/qhangups/archive/v$pkgver.tar.gz)

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python setup.py install --root="$pkgdir"
}

# vim:set ts=2 sw=2 et:
