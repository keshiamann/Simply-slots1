[app]
title = Simply Slots Casino
package.name = simplyslots
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg,ttf,txt,json,wav
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 21
android.permissions = INTERNET
entrypoint = main.py

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.ndk = 25b
android.ndk_api = 21
target.arch = armeabi-v7a
android.archs = armeabi-v7a
