This is miniSW



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

Once you're OK with the app, launch :

```
pyinstaller build.spec
```
