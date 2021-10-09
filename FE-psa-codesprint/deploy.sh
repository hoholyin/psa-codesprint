git checkout gh-pages
git pull origin master
ng build --prod --base-href "https://hoholyin.github.io/psa-codesprint/"
npx angular-cli-ghpages --dir=dist/psa-codesprint
git checkout master
