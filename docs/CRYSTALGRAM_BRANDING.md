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
- Intro textures use supplied CrystalGram artwork. The native intro rectangle is square to match it; the existing animation and resource/JNI names remain intact.
- Telegram call/service marks and the generic airplane icon remain. Historical upstream changelog artwork and screenshots remain as upstream history, not current CrystalGram release marketing.

## Compatibility and update integration

The Lollipop flavor remains API 21–22, including Android 5.1.1. No SDK levels, flavor dependencies, TDLib implementation, authentication requests, networking, theme format, or protocol identifiers were changed.

`AppUpdater.java` no longer offers Telegram X channel APKs to an application with a different ID. Those packages cannot update independently signed CrystalGram installations. Urgent-update notices and server-suggested downloads also keep the configured fork release destination. CrystalGram releases remain available through the configured release link; a separate automatic fork update feed is not implemented.

Downloaded translations and translation fetching are unchanged, as requested. Server-provided text can therefore differ from bundled branding and wording.

## Existing resource errors repaired

Resource compilation of the original committed strings failed on:

- Unescaped apostrophes in `Page2Message`, `SentFragmentCode`, and `OpenFragment`.
- Stray `ew` text outside the `GroupChannelUnlink` resource element.

Only escaping and invalid out-of-element text were corrected. Displayed wording, humor, criticism, resource names, and format arguments were preserved.

## Fragment review

| Resource | Finding | Result |
| --- | --- | --- |
| `LinkPurchasable` | Mentions buying an unavailable group/channel link with crypto. | Flagged for owner review; existing critical wording retained. |
| `UsernamePurchasable` | Mentions buying an unavailable username with crypto. | Flagged for owner review; existing critical wording retained. |
| `EditBotUsernameHint` | Already says the crypto upsell was shattered. The caller still constructs a Fragment URL and supplies it as a format argument, but this bundled string has no placeholder/link. | Existing wording retained. |
| `SentFragmentCode` | Navigation instructions for existing Fragment-number accounts; not a purchase prompt. | Exact “Funny Money Account” wording retained, with required apostrophe escaping. |
| `OpenFragment` | Was appended as a clickable marketplace link in the Fragment login prompt. | Removed from the rendered login prompt in `PasswordController.java`, including the `fragment.url` click handler. Resource key retained for compatibility. |
| `AnonymousNumbers` | Country/number selector label for +888 numbers. | Retained; no purchase prompt or link. |

The username purchase strings currently have no `%1$s` placeholder, so the Fragment URL constructed by `EditUsernameController` is not inserted into their bundled text. No other bundled explicit Fragment purchase prompt was found. Downloaded translations are outside this review.

## Validation

Run `python3 scripts/validate-crystalgram-branding.py` from any directory. It checks XML, resource keys and format arguments against Git HEAD, selected authored strings, service attribution, launcher dimensions and original asset bytes (when the sibling asset directory is present), adaptive artwork, default identity, manifest references, and API 21–22 configuration.

Both main resources and the Android 8+ resource overlay compile with Android AAPT2 8.9.1-12782657. `git diff --check` passes. Full Gradle and device validation are recorded below after the build attempt.
