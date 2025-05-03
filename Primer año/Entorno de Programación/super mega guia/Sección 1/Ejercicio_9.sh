mkdir -p ./dir.a/dir.b ./dir.a/dir.c
touch ./dir.a/dir.b/file.a ./dir.a/dir.b/file.b
ln -s ./dir.a/dir.c/link.a ./dir.a/dir.b/file.a

