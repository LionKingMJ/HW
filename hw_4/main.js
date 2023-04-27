

function cal() {
    //전문가
    const subject = document.getElementById('subject').value;
    document.getElementById("r_subject").innerText = subject;
    //시간
    const studyHoursPerDay = Number(document.getElementById("study-hours").value);
    const totalStudyHours = 10000;
    const totalStudyDays = Math.ceil(totalStudyHours / studyHoursPerDay);
    document.getElementById("r_date").innerText = totalStudyDays;
    //document.getElementById("r_date").textContent = `${totalStudyDays}일 동안 공부해야 합니다.`;
    show()
}

function show(){
    document.getElementById("ShowInfo").style.display = 'block';
}

function clip(){

	var url = '';
	var textarea = document.createElement("textarea");
	document.body.appendChild(textarea);
	url = window.document.location.href;
	textarea.value = url;
	textarea.select();
	document.execCommand("copy");
	document.body.removeChild(textarea);
	alert("URL이 복사되었습니다.")
}

function showPopup() {
    const popup = document.getElementById("popup");
    const popupContent = document.getElementById("popup-content");
    const closeButton = document.getElementById("close-button");

    // 팝업 내용이 화면 중앙에 위치하도록 설정
    popupContent.style.top = "50%";
    popupContent.style.left = "50%";
    popupContent.style.transform = "translate(-50%, -50%)";

    // 레이어팝업 보이기
    popup.style.display = "block";

    // 닫기 버튼 클릭 시 레이어팝업 닫기
    closeButton.addEventListener("click", function() {
        popup.style.display = "none";
    });
}