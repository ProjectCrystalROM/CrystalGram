# CrystalGram branding and integration

CrystalGram is the independent Project Crystal client for Telegram. Telegram operates the messaging service. Telegram X, TDLib, GPLv3, and third-party attribution remain intact.

## Identity and assets

- `local.properties.sample`: default application ID `ing.crystaliz.crystalgram`, label `CrystalGram`, Project Crystal repository and release links. Existing private `local.properties` overrides still take precedence; release builders must use the fork identity and their own signing/API/Firebase configuration.
- `settings.gradle.kts`: project name `CrystalGram`. Java/JNI namespaces and upstream resource identifiers remain unchanged for compatibility.
- `app/src/main/AndroidManifest.xml`: foreground-service description identifies CrystalGram. Application, intent, account, and shortcut labels/icons already reference the shared resources. Provider authorities and account types already derive from the application ID.
- `SyncAdapter.java`: Android sync account name follows the configured client name.
- `values/strings.xml` and `local_strings.xml`: bundled client labels, permission instructions, notifications, diagnostics, update prompts, and version signatures identify CrystalGram. Client support/download links point to the existing ProjectCrystalROM/CrystalGram repository. Service support, Telegram Premium, Telegram cloud, account services, and TDLib diagnostics remain attributed to their operators.
- `OpenSourceGuide` explicitly credits Telegram X and TDLib, identifies the independent Project Crystal fork, and names GPLv3.
- Supplied 48/72/96/144/192px PNGs are copied unchanged into mdpi/hdpi/xhdpi/xxhdpi/xxxhdpi launcher and round-launcher resources. `logo_middle` uses the same artwork. The existing `images/logo.png` already matched the supplied 512px logo.
- Android 8+ adaptive launchers use the supplied PNGs over a dark teal background, inset into the adaptive safe area. Old adaptive plane layers are removed.
- A code-native crystal silhouette supplies the Android 5+ notification icon, themed adaptive icon, passcode mark, and source-code menu mark. The legacy notification fallback uses the supplied bitmap.
- Intro textures use supplied CrystalGram artwork. The native intro rectangle is square and its anchor is centered to match it; the existing animation and resource/JNI names remain intact.
- Telegram call/service marks and the generic airplane icon remain. Historical upstream changelog artwork and screenshots remain as upstream history, not current CrystalGram release marketing.

## Compatibility and update integration

The Lollipop flavor remains API 21–22, including Android 5.1.1. No SDK levels, flavor dependencies, TDLib implementation, authentication requests, networking, theme format, or protocol identifiers were changed.

`AppUpdater.java` no longer offers Telegram X channel APKs to an application with a different ID. Those packages cannot update independently signed CrystalGram installations. Urgent-update notices and server-suggested downloads also keep the configured fork release destination. CrystalGram releases remain available through the configured release link; a separate automatic fork update feed is not implemented.

Bundled English is authoritative for ordinary resources and plural forms, so downloaded English does not override CrystalGram branding or authored wording. Cloud-only ordinary keys and other language packs retain the upstream translation path. Translation fetching is unchanged.

## Existing resource errors repaired

Resource compilation of the original committed strings failed on:

- Unescaped apostrophes in `Page2Message`, `SentFragmentCode`, and `OpenFragment`.
- Stray `ew` text outside the `GroupChannelUnlink` resource element.

Only escaping and invalid out-of-element text were corrected. Displayed wording, humor, criticism, resource names, and format arguments were preserved.

## Fragment review

| Resource | Finding | Result |
| --- | --- | --- |
| `LinkPurchasable` | Mentions buying an unavailable group/channel link with crypto. | Cleared by owner review: intended critical wording confirmed; no bundled clickable link. |
| `UsernamePurchasable` | Mentions buying an unavailable username with crypto. | Cleared by owner review: intended critical wording confirmed; no bundled clickable link. |
| `EditBotUsernameHint` | Already says the crypto upsell was shattered. The caller still constructs a Fragment URL and supplies it as a format argument, but this bundled string has no placeholder/link. | Existing wording retained. |
| `SentFragmentCode` | Navigation instructions for existing Fragment-number accounts; not a purchase prompt. | Exact “Funny Money Account” wording retained, with required apostrophe escaping. |
| `OpenFragment` | Was appended as a clickable marketplace link in the Fragment login prompt. | Removed from the rendered login prompt in `PasswordController.java`, including the `fragment.url` click handler. Resource key retained for compatibility. |
| `AnonymousNumbers` | Country/number selector label for +888 numbers. | Retained; no purchase prompt or link. |

The username purchase strings currently have no `%1$s` placeholder, so the Fragment URL constructed by `EditUsernameController` is not inserted into their bundled text. No other bundled explicit Fragment purchase prompt was found. Downloaded translations are outside this review.

## Validation

Run `python3 scripts/validate-crystalgram-branding.py` from the repository root (or use its absolute path from elsewhere). Use `--base fe76f810` to compare the completed branding commit against its pre-branding parent. It checks XML, resource keys and format arguments against Git HEAD or the supplied `--base` revision, selected authored strings, service attribution, launcher dimensions and original asset bytes (when the sibling asset directory is present), adaptive artwork, default identity, manifest references, and API 21–22 configuration.

Both main resources and the Android 8+ resource overlay compile with Android AAPT2 8.9.1-12782657. `git diff --check` passes.

### Build and device validation — 2026-10-29

The Lollipop debug build succeeds with JDK 25 and the SDK/NDK versions in `version.properties`. ARMv7, ARM64, x86 and x86_64 APKs were produced. The ARMv7 package was verified as `ing.crystaliz.crystalgram`, label `CrystalGram`, minimum SDK 21, with valid v1/v2 signatures.

The maintainer confirmed installation, Telegram login, corrected English intro wording, centered intro artwork, and the light and dark palettes on the target device. Those initial results used debug builds. A subsequent dedicated-key Lollipop release build passed on-device installation, Telegram login, chat browsing, light/dark colors, strings and actual incoming push delivery through microG on the LG K7/MS330 running AOSP 5.1.1. ARM64, x86 and x86_64 release APKs pass package/signature checks but have not been hardware-tested.

Earlier failures came from incomplete submodule checkouts, missing SDK packages/licenses, and empty proxy environment values. They were resolved before successful builds. Keep configuration cache enabled while Isolated Projects is enabled.

```sh
bash ./gradlew :app:validateApiTokens :app:assembleLollipopDebug --no-daemon --console=plain
```

## Local credentials

Set `telegram.api_id` and `telegram.api_hash` in ignored `local.properties`. Supply your own `app/google-services.json` matching `ing.crystaliz.crystalgram`; this file is ignored and must not be committed. The upstream Firebase configuration has been removed from tracking. Signing keys and their passwords must also remain local.

Push testing requires a non-experimental configuration: `app.experimental=false`, signing enabled, and `keystore.file` pointing to a local signing-properties file. Experimental builds disable Firebase integration and push registration. Use a debug key for development and a separate appropriate release-signing configuration for distribution.

## Project Crystal palette

The Blue base theme (also inherited by Classic), Night Blue, the intro circle, and system fallback colors use pale lavender `#E9D8F5` and deep amethyst `#4B3069`. Existing theme IDs and resource names remain unchanged. Semantic red/green colors, contact identity hues, photo editor swatches and LED choices remain intact.

Lavender fills and highlights pair with dark purple foregrounds in light mode. Dark mode uses lavender accents and amethyst surfaces, with `#30203F` and `#65477F` variants to distinguish backgrounds and controls. Light-mode secondary text uses amethyst and muted icons use `#685875`; the contrast correction preserves the effective Night Blue palette exactly.

Lavender/amethyst contrast is 8.10:1; amethyst/white is 10.90:1. Corrected light foreground pairs on white, light gray and lavender are at least 4.81:1. The maintainer confirmed both palettes on-device.


## First signed release — 2026-10-29

CrystalGram 0.29.1.1820 Lollipop release APKs use a dedicated RSA3072 application
signer, separate from Project Crystal ROM signing keys. Package ID remains
`ing.crystaliz.crystalgram`; minimum API21, target API37. The release signer is:

```
CN=Crystalgram, O=ProjectCrystalROM
SHA-256: 1fd6c23613c39f4414911e6e217d2708f2fa92933263848da0a54b6d6784e503
```

Build with the existing private release-signing configuration and valid local
Telegram/Firebase configuration (never commit those files):

```sh
bash ./gradlew :app:validateApiTokens :app:assembleLollipopRelease --no-daemon --console=plain
```

All four architecture APKs pass v1 signature verification with that signer and
are non-debuggable. Only ARMv7 has the hardware validation described above.
Development APKs signed with the Android debug key cannot update directly to
these release APKs; preserve anything needed before uninstalling the debug app.
Future releases must retain the release signing identity for update compatibility.
