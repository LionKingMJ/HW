function 다짐제출() {
  var 다짐1 = document.getElementById("다짐1").value;
  var 다짐2 = document.getElementById("다짐2").value;
  var 다짐제출 = document.getElementById("다짐제출");
  var 다짐2다시 = Math.round(10000 / 다짐2);
  var 훈련go공유 = document.getElementsByClassName("훈련go공유")[0];

  if (isNaN(다짐2)) {
    alert("훈련시간은 숫자를 입력해주세요");
  } else {
    훈련go공유.style.display = "block";

    다짐제출.innerHTML =
      "당신은 <span style='font-size:45px; font-weight:bold'>" +
      다짐1 +
      "</span>전문가가 되기 위해서 <br> 대략 <span style='font-size:45px; font-weight:bold'>" +
      다짐2다시 +
      "</span>일 이상 훈련하셔야 합니다! :)";
  }
}

function 훈련go() {
  var 훈련go누를시 = document.getElementsByClassName("훈련go누를시")[0];

  훈련go누를시.style.display = "flex";
  window.scrollTo(0, 300);
}

function 공유하기() {
  alert("url이 복사되었습니다");
  copyToClipBoard("https://manition.tistory.com/8");
}

function 진짜훈련() {
  var 훈련go누를시 = document.getElementsByClassName("훈련go누를시")[0];
  훈련go누를시.style.display = "none";
  window.open("https://techit.education/", "_blank");
}
