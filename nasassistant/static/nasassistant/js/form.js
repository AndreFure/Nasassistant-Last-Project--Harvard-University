

document.addEventListener("mousemove", parallax);
function parallax(e) {
  this.querySelectorAll('.layer').forEach(layer => {
    const speed = layer.getAttribute('data-speed')

    const x = (window.innerWidth - e.pageX * speed) / 100
    const y = (window.innerHeight - e.pageY * speed) / 100

    layer.style.transform = `translateX(${x}px) translateY(${y}px)`
  })
}

let cursor = document.getElementById('cursor');

document.addEventListener('mousemove', function (e) {
  let x = e.clientX;
  let y = e.clientY;
  cursor.style.left = x + "px";
  cursor.style.top = y + "px";
});

const button = document.querySelector('btnmsj');

button.forEach(btn => {
  btn.addEventListener('click', function (e) {
    let x = e.clientX - e.target.offsetLeft;
    let y = e.clientY - e.target.offsetTop;
    let ripples = document.createElement('span');
    ripples.style.left = x + 'px';
    ripples.style.top = y + 'px';
    this.appendChild(ripples);

    setTimeout(() => {
      ripples.remove()
    }, 1000);
  })
})

