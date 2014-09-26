# Maintainer: Michal Krenek (Mikos) <m.krenek@gmail.com>
pkgname=qhangups
pkgver=1.0
pkgrel=1
pkgdesc="Alternative client for Google Hangouts written in PyQt"
arch=('any')
url="https://github.com/xmikos/qhangups"
license=('GPL3')
depends=('hangups-git' 'python-pyqt' 'python-quamash' 'python-appdirs')
source=(https://github.com/xmikos/qhangups/archive/v$pkgver.tar.gz)
md5sums=('2a2e0202263de9dc959ef0abe6ef1bdd')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  python2 setup.py build
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  python2 setup.py install --root="$pkgdir"
}

# vim:set ts=2 sw=2 et:
