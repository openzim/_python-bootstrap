search_dir=/src/dist/*.tar.gz
for entry in $search_dir
do
  pip install --no-cache-dir "$entry"
done
