let userScore = 0;
let compScore = 0;

const choice = document.querySelectorAll(".choice");
const msg = document.querySelector("#msg");

const userScorePara = document.querySelector("#user-score");
const compScorePara = document.querySelector("#comp-score");


const genCompChoice = () => {
    const options = ["stone","paper","scissor"];
    const randIdx = Math.floor(Math.random() * 3);
    return options[randIdx];

}

const drawGame = () => {
    msg.innerText="Game Draw, play Again.";
    msg.style.backgroundColor = "orange";
}
const showWinner = (userWin) => {
    if(userWin) {
        userScore++;
        userScorePara.innerText=userScore;
        msg.innerText ="you won.";
        msg.style.backgroundColor = "green";
    } else {
        compScore++;
        compScorePara.innerText=compScore;
        msg.innerText = "you lost."
        msg.style.backgroundColor = "red";  
      }
}

const playGame = (userChoice) => {
    console.log("user choice = " , userChoice);
    const CompChoice = genCompChoice();
    console.log("Computer choice = ",CompChoice)

    if(userChoice === CompChoice ){
        drawGame();
    } else {
        let userWin = true;
        if(userChoice ==="rock") {
           userWin = CompChoice ==="paper" ?  false : true;

        } else if(userChoice === "paper") {
             userWin = CompChoice === "scissor" ? false : true;
        } else {
            userWin= CompChoice === "rock" ? false : true;
        }
        showWinner(userWin)
    }

};


choice.forEach((choice) => {
    choice.addEventListener("click" ,()=> {
        const userChoice = choice.getAttribute("id");
        playGame(userChoice);

    });
});