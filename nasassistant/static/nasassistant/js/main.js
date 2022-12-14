let but = document.querySelector('.but');
let h3Title = document.getElementById('h3Title');
let dayP = document.getElementById('dayP');
let dayP1 = document.getElementById('dayP1');
let expl = document.getElementById('explan');
let dayButtonD = document.getElementById('dayButtonD');
let moonPicture = document.getElementById('moonPicture');
let moonContainer1 = document.querySelector('.moonContainer1');



dayButtonD.addEventListener('click', () => {
  sendApiRequest();
});

async function sendApiRequest() {
  let API_KEY = "DI7BkDgYKcjL4zdB1f0hNpkthVj7MG2ccs6CjYdM";
  let response = await fetch(`https://api.nasa.gov/planetary/apod?api_key=${API_KEY}`);
  let data = await response.json();
  let title = data.title;
  let url = data.url;
  let explanation = data.explanation;
  let titleh3 = createTitleElement(title);
  document.getElementById('explan').innerHTML = explanation;
  expl.classList.add('explaP');
  moonPicture.classList.add('imgSize');
  moonContainer1.classList.add('mC1');
  moonPicture.src = url;
  h3Title.appendChild(titleh3);
}

//h3Title

function createTitleElement(data) {
  let titleh3 = document.createElement('h3');
  titleh3.className = "titleh3Style";
  let titleElement = document.createTextNode(data);
  titleh3.appendChild(titleElement);
  return titleh3;
}





















