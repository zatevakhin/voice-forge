# CHANGELOG


## v0.1.4 (2025-04-19)

### Bug Fixes

- Packages version bump for compatibility with my projects
  ([`03d2b3c`](https://github.com/zatevakhin/voice-forge/commit/03d2b3c2b5d2d2b66857bb8ebdb728bde85d6fb5))

### Continuous Integration

- Fixed broken ci
  ([`24cbce9`](https://github.com/zatevakhin/voice-forge/commit/24cbce91c3eb6404b842b4b028afd0e3883118e8))


## v0.1.3 (2024-07-05)

### Bug Fixes

- Pinned onnxruntime due to issues in new versions.
  ([`bf7d806`](https://github.com/zatevakhin/voice-forge/commit/bf7d8066f6cb5f4501ab31d29c51ccaead487867))

- https://github.com/rhasspy/piper/issues/520 -
  https://github.com/microsoft/onnxruntime/issues/20877

### Chores

- Added `portaudio` as deps in devenv.
  ([`80f47ad`](https://github.com/zatevakhin/voice-forge/commit/80f47ad306af042072dc2e8fcfa51c58416422c6))

### Continuous Integration

- Fixed pipeline, release `dist/*` contents
  ([`fae7b39`](https://github.com/zatevakhin/voice-forge/commit/fae7b39a6b0c83840a01beac0e209efaa214fbe2))

- Small fixed and caching optimizations
  ([`d6fe84f`](https://github.com/zatevakhin/voice-forge/commit/d6fe84ffcfa757a98f24026200c43482d0ececf0))


## v0.1.2 (2024-06-29)

### Bug Fixes

- Piper and Sounddevice as optional.
  ([`3fcf4a6`](https://github.com/zatevakhin/voice-forge/commit/3fcf4a66c6c033a4949248181c1893398ad73201))

### Chores

- Using nix devenv for deps management.
  ([`4d792ea`](https://github.com/zatevakhin/voice-forge/commit/4d792ea285d0c54e621aaa93a950f832829a6b57))

### Continuous Integration

- Added CI/CD pipeline
  ([`432e87f`](https://github.com/zatevakhin/voice-forge/commit/432e87f2e5145b1fc59b757a60776d0b097608e1))

- Fixed linter errors


## v0.1.1 (2024-05-06)

### Features

- Added model downloading ability by using hf-hub
  ([`383f6bb`](https://github.com/zatevakhin/voice-forge/commit/383f6bb6ffe89c717fd0c03ab2b84ab5945ae55a))


## v0.1.0 (2024-01-18)

### Features

- Minimal text-to-speech using piper-tts
  ([`6644845`](https://github.com/zatevakhin/voice-forge/commit/664484569cb124bdd016de247287dabcbb2f8ae9))
