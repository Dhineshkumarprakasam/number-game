var displayScore = document.getElementById("score");
var score = 0;
var chance = 3;
var level = document.getElementById('lev');

function submit() {
    var min, max;
    if (level.textContent.includes("Easy")) {
        min = 1;
        max = 9;
    } else if (level.textContent.includes("Medium")) {
        min = 1;
        max = 5;
    } else if (level.textContent.includes("Difficult")) {
        min = 1;
        max = 3;
    }
    
    var randomNumber = getRandomInteger(min, max);
    var user = document.getElementById("number-box");
    var userValue = Number(user.value);

    if (userValue < min || userValue > max) {
        alert("Out of range");
        document.getElementById("number-box").value=''
        return;
    }

    document.getElementById("random").textContent = "Computer : " + randomNumber;
    document.getElementById("user").textContent = "User : " + userValue;
    if (chance > 0) {
        if (randomNumber != userValue) {
            score = score + userValue;
            displayScore.textContent = "Score : " + score;
            document.getElementById("number-box").value=''
        } else if (randomNumber == userValue) {
            chance = chance - 1;
            alert(chance + " chances left");
            document.getElementById('chance').textContent = "Chance : " + chance;
            document.getElementById("number-box").value=''
        }
    }
    if(chance==0){
        alert("game over")
        submit_score(score);
    }
}

function getRandomInteger(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function submit_score(finalScore) {
    document.getElementById("finalScore").value = finalScore;
    document.getElementById("saveform").submit();
}

document.addEventListener('keydown', function(event) {
    var user = document.getElementById("number-box");
    user.focus();

    if (event.key === "Enter") {
        submit();
    }
});