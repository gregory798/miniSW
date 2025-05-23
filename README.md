steps for modification + verifications :

-<h1>Hello World v1</h1>
+<h1>Hello World v2</h1>

Save

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