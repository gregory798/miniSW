steps for modification + verifications :

```
-<h1>Hello world !</h1>
+<h1>Hello world 2 !</h1>
```

```
cd front
```

```
npm run generate
```

```
cd ..
```

```
rm -rf back/static
```

```
mv front/.output/public back/static
```

```
python3.10 run.py
```

```
source venv-build/bin/activate
```

```
pyinstaller build.spec
```
