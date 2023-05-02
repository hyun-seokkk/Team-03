const rating = document.querySelector('#rating');
const checks = document.querySelectorAll('.star-check');
console.log(checks);
const totalChecks = checks.length;
const checkWidth = 10;

function setRatingWidth(width) {
  const checkedChecks = Math.ceil(width / checkWidth);
  console.log(checkedChecks);
  for (let i = 0; i < totalChecks; i++) {
    checks[i].classList.remove('checked');
    if (i < checkedChecks) {
      checks[i].classList.add(`star-check-${i+1}`);
      checks[i].classList.add('checked');
    } else {
      checks[i].classList.remove(`star-check-${i+1}`);
    }
  }
}

rating.addEventListener('mousemove', (event) => {
  const ratingRect = rating.getBoundingClientRect();
  const mouseX = event.clientX - ratingRect.left;
  const width = Math.min(Math.max(mouseX, 0), ratingRect.width);
  setRatingWidth(width);
});

rating.addEventListener('click', (event) => {
  const ratingRect = rating.getBoundingClientRect();
  const mouseX = event.clientX - ratingRect.left;
  const width = Math.min(Math.max(mouseX, 0), ratingRect.width);
  setRatingWidth(width);
});
