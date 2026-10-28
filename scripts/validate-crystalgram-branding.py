#!/usr/bin/env python3
"""Check bundled branding without Gradle, Android SDK, or initialized submodules."""
from pathlib import Path
import re
import struct
import subprocess
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
RES = ROOT / 'app/src/main/res'

def check(condition, message):
    if not condition:
        raise SystemExit(message)

def strings(data):
    return {e.attrib['name']: ''.join(e.itertext()) for e in ET.fromstring(data).findall('string')}

for path in (ROOT / 'app/src').rglob('*.xml'):
    ET.parse(path)
current = strings((RES / 'values/strings.xml').read_bytes())
for key, value in current.items():
    check('Telegram X' not in value or key == 'OpenSourceGuide', f'Old client identity: {key}')
    check(not re.search(r"(?<!\\)'", value), f'Unescaped apostrophe: {key}')

# Compare with the checked-in tree to catch accidental resource/API changes.
for name in ('strings.xml', 'local_strings.xml'):
    path = f'app/src/main/res/values/{name}'
    original = strings(subprocess.check_output(['git', 'show', f'HEAD:{path}'], cwd=ROOT))
    updated = strings((ROOT / path).read_bytes())
    check(original.keys() == updated.keys(), f'Resource keys changed: {name}')
    for key in original:
        pattern = r'%(?:\d+\$)?[-#+ 0,(]*\d*(?:\.\d+)?[a-zA-Z%]'
        check(re.findall(pattern, original[key]) == re.findall(pattern, updated[key]), f'Format arguments changed: {key}')
        if any(term in original[key] for term in ('Telegram Premium', 'Telegram servers', 'Telegram cloud', 'Telegram API')):
            check(original[key].count('Telegram') == updated[key].count('Telegram') or 'Telegram X' in original[key], f'Service attribution changed: {key}')
    for key in ('Page1Message', 'Page2Message', 'StartMessaging', 'AnonymousAdmin', 'EventLogPromotedRemainAnonymous', 'AndroidVersionWarning', 'EditBotUsernameHint', 'LinkPurchasable', 'UsernamePurchasable', 'SentFragmentCode', 'OpenFragment'):
        if key in original:
            check(original[key].replace("\\'", "'") == updated[key].replace("\\'", "'"), f'Authored wording changed: {key}')

for density, size in [('mdpi',48), ('hdpi',72), ('xhdpi',96), ('xxhdpi',144), ('xxxhdpi',192)]:
    launcher = RES / f'mipmap-{density}/app_launcher.png'
    data = launcher.read_bytes()
    check(struct.unpack('>II', data[16:24]) == (size,size), f'Wrong density: {density}')
    check(data == (RES / f'mipmap-{density}/app_launcher_round.png').read_bytes(), f'Round icon differs: {density}')
    supplied = ROOT.parent / f'crystalgram_icons/icon-{size}x{size}.png'
    if supplied.exists():
        check(data == supplied.read_bytes(), f'Launcher differs from supplied asset: {density}')
    adaptive = ROOT / f'app/src/sinceOreo/res/mipmap-{density}-v26/app_launcher_art.png'
    check(data == adaptive.read_bytes(), f'Adaptive artwork differs: {density}')

props = (ROOT / 'local.properties.sample').read_text()
check('app.id=ing.crystaliz.crystalgram' in props and 'app.name=CrystalGram' in props, 'Wrong default identity')
config = (ROOT / 'buildSrc/src/main/kotlin/Config.kt').read_text()
check(re.search(r'flavor = "lollipop",\s*minSdk = 21,\s*maxSdk = 22', config), 'Lollipop support changed')
manifest = (ROOT / 'app/src/main/AndroidManifest.xml').read_text()
check('android:label="@string/AppName"' in manifest, 'Wrong application label')
check('android:icon="@mipmap/app_launcher"' in manifest, 'Wrong launcher reference')
print('PASS: XML, resource keys, format arguments, authored wording, service attribution, density assets, identity, and API 21–22 configuration')
