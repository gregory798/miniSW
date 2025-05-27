# miniSW : Starter Template for Full-Stack Desktop Apps (MacOS, Linux, Windows) using Nuxt 3 & FastAPI


<p align="left">
  <a href="https://nuxt.com" target="_blank">
    <img src="https://img.shields.io/badge/Nuxt-3.x-00DC82?logo=nuxt.js&logoColor=white" alt="Nuxt 3" />
  </a>
  <a href="https://fastapi.tiangolo.com" target="_blank">
    <img src="https://img.shields.io/badge/FastAPI-0.110+-009688?logo=fastapi&logoColor=white" alt="FastAPI" />
  </a>
  <a href="https://www.python.org/" target="_blank">
    <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" alt="Python" />
  </a>
  <img src="https://img.shields.io/badge/OS-macOS%20|%20Linux%20|%20Windows-blue" alt="OS" />
  <img src="https://img.shields.io/badge/Bundled%20with-PyInstaller-yellow" alt="PyInstaller" />
</p>

![miniSW GIF](https://s14.gifyu.com/images/bxMCL.gif)


# Development

If you want to make modifications in the front-end :

go to /front and make your changes:

```
-<h1>Hello world !</h1>
+<h1>Hello world 2 !</h1>
```

then build the app :

```
npm run build
```
then go to root

```
cd ..
```
then remove teh static folder
```
rm -rf back/static
```
then move the front-end output to static
```
mv front/.output/public back/static
```
then run the app :
```
python3.10 run.py
```

Once you're OK with the app, run pyinstaller :

```
pyinstaller build.spec
```

You will find the app in the /dist folder
