# CrystalGram 💎

**Telegram X, reimagined for Project Crystal.**

CrystalGram is a Project Crystal-branded fork of [Telegram X](https://github.com/TGX-Android/Telegram-X), intended to provide a familiar Telegram experience on devices running Project Crystal Android distributions.

Built upon Telegram X and its existing support for Android Lollipop, CrystalGram brings Telegram messaging into the Project Crystal ecosystem without reinventing an already capable client.

## Purpose

CrystalGram exists to provide a consistent, recognizable messaging application that can be included with Project Crystal ROMs.

The focus is on branding, integration, and maintaining compatibility with the Android versions supported by Project Crystal.

CrystalGram is not intended to replace Telegram X's underlying messaging architecture or independently reimplement Telegram's protocols.

## Compatibility

Telegram X already supports Android 5.1.1 through its existing Android compatibility configurations.

CrystalGram inherits that support from upstream, subject to changes introduced by the fork.

The LG K7 (MS330), running Project Crystal's AOSP 5.1.1 build, is an initial integration target.

## Development Status

**Bundled branding integrated; full build and device validation pending.**

The default application ID is `ing.crystaliz.crystalgram`. See [branding decisions, Fragment review, and validation](docs/CRYSTALGRAM_BRANDING.md) for the integration details and remaining build requirements.

## Checkout dependencies

CrystalGram uses Git submodules for TDLib, vkryl, and native libraries. A normal clone can leave these directories empty; Git LFS does not populate them.

After cloning, fetch the pinned dependencies and their nested submodules:

```sh
git submodule update --init --recursive --jobs 4
```

Do not use `--remote` for normal builds: it advances dependencies instead of using the revisions recorded by CrystalGram. Check `git submodule status --recursive`; a leading `-` means a dependency is still uninitialized, while `+` means its checkout differs from the recorded revision.

The current build tooling requires JDK 25. Android SDK, NDK, CMake, and build-tools versions are recorded in `version.properties`; dependency checkout alone does not install them. See [branding and build validation](docs/CRYSTALGRAM_BRANDING.md) for credential setup and validation status.

## Upstream and Attribution

CrystalGram is based on [Telegram X](https://github.com/TGX-Android/Telegram-X), powered by [TDLib](https://core.telegram.org/tdlib).

All original development credit belongs to the Telegram X, TDLib, and respective third-party contributors.

CrystalGram is an independent Project Crystal fork and is not affiliated with, endorsed by, or officially maintained by Telegram.

## License

CrystalGram retains Telegram X's GNU General Public License version 3 (GPLv3) licensing obligations.

See the repository's `LICENSE` and third-party notices for details.

---

**Project Crystal** — https://crystaliz.ing

*Fallen Doesn't Mean Finished.* 💎
