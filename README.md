# Atom Notify

We wanted to write a notification system from scratch for Ozon but it turned out capturing signals was [quite difficult](https://github.com/mayppong/atom-notify/commit/e1326c7fac846429d3fe39be90fda3a23987718f). Instead we decided to use the great work of [Jens Lody](https://github.com/jenslody) on [Panel OSD](https://github.com/jenslody/gnome-shell-extension-panel-osd) and just tweak the default settings.

### Building

Make sure you have the following dependencies installed:
* `pkg-config`
* `git`
* `zip`
* `gnome-common`
* `autoconf`
* `automake`
* `gnome-tweak-tool`

Run the following commands:

```bash
cd ~ && git clone git://github.com/ozonos/nsion-panel-osd.git
cd ~/gnome-shell-extension-panel-osd
./autogen.sh && make local-install
```

