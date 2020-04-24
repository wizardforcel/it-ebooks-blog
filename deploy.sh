rm -rf public
hexo g
cd public
touch .nojekyll
git init
git config user.name wizardforcel
git config user.email 562826179@qq.com
git add -A
git commit -am "$(date "+%Y-%m-%d %H:%M:%S")"
git push https://github.com/it-ebooks/it-ebooks.github.io.git master:master -f
