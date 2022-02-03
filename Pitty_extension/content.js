//CODE RETRIEVED FROM DAN SHIFFMAN'S CODING CHALLENGE#82
//link: https://www.youtube.com/watch?v=8zMMOdI5SOk&list=PLRqwX-V7Uu6bL9VOMT65ahNEri9uqLWfS&index=5

console.log('MR WORDWIDE');

let filenames = [
  'pitty.jpeg'
];

let imgs = document.getElementsByTagName('img');

for (let imgElt of imgs) {
  let r = Math.floor(Math.random() * filenames.length);
  let file = 'images/' + filenames[r];
  let url = chrome.extension.getURL(file);
  imgElt.src = url;
  console.log(url);
}
