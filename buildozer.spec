

[app]

title = NoteLock
package.name = notelock
package.domain = org.notelock

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt,pdf

version = 1.0

requirements = python3,kivy,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,RECORD_AUDIO

android.api = 35
android.minapi = 21

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True

android.debug = 1

android.release = 0

android.ndk = 27b
android.sdk = 35

android.accept_sdk_license = True

p4a.bootstrap = sdl2

[buildozer]

log_level = 2
warn_on_root = 1
