#!/usr/bin/env seed

/*
 * PO Updater for Atom Notify. This file is part of Atom Notify, a fork
 * of gnome-shell-extension-panel-osd for OzonOS.
 *
 *     Copyright (C) 2012
 *     Christian METZLER <neroth@xeked.com>
 *     2014 Jens Lody <jens@jenslody.de>
 *
 * Atom Notify is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * Atom Notify is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with Atom Notify. If not, see <http://www.gnu.org/licenses/>.
 *
 */

Gio = imports.gi.Gio;

print("Generate atom-notify.pot");
var xgettext = Seed.spawn("xgettext -o atom-notify.pot --from-code=utf-8 --keyword=_ --keyword=translatable -f POTFILES.in");

if (xgettext.stderr)
    print(xgettext.stderr);
else {
    var file = Gio.file_new_for_path(".");
    var enumerator = file.enumerate_children("standard::name,standard::size");
    var linguas = "";
    var n = "";
    var i = 0;
    while (child = enumerator.next_file())
        if (child.get_name().search(/.po$/) != -1) {
            print("Generate " + child.get_name());
            linguas += n + (child.get_name().split(".po")[0]);
            Seed.spawn("msgmerge -U " + child.get_name() + " atom-notify.pot");
            n = "\n";
            i++;
        }

    print("Write LINGUAS file");
    Gio.simple_write("LINGUAS", linguas);
    print("Successfully generated " + i + " entry");
}
