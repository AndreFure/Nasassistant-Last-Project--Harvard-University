let marsExpl = document.getElementById('marsExplan');
let marsPicture = document.getElementById('marsPicture');
let curiosityContainer1 = document.querySelector('.curiosityContainer1');

/*Mars------------------------*/

let count = 0;
function count1() {
  sendApiRequestMars();
  count++;
}

async function sendApiRequestMars() {
  let API_KEY = "DI7BkDgYKcjL4zdB1f0hNpkthVj7MG2ccs6CjYdM";
  let response = await fetch(`https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=${API_KEY}`);
  let dataMars = await response.json();
  let marsUrl = dataMars.photos[count].img_src;
  marsPicture.src = marsUrl;
  let marsExplanation = dataMars.photos[count].earth_date;
  let marsExplanation1 = `Date: ${marsExplanation}. Look at another photo.`;
  document.getElementById('marsExplan').innerHTML = marsExplanation1;
  marsExpl.classList.add('explaP');
  marsPicture.classList.add('imgSize');
  curiosityContainer1.classList.add('mC2');
  return dataMars;
}