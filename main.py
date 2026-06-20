from flask import Flask,request,render_template,redirect
import submain

app=Flask(__name__)
board=[""]*9
@app.route("/",methods=["GET","POST"])
def home():
   
    global board
  
    if request.method=="POST":
        pos=int(request.form["cell"])
        if board[pos]=="":
            board[pos]="X"
            
            board=submain.ai_move(board)

    message=""

    if submain.check_winner(board,"X"):
        message="X Wins"
        

    elif submain.check_winner(board,"O"):
        message="O Wins"
        
                      
    elif "" not in board:
        message="Draw"

    return render_template("Ui.html",board=board,message=message)

@app.route("/restart",methods=["POST"])
def restart():
    global board
    board=[""]*9
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)

    
    



