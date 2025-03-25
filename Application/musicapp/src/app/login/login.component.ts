import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { User } from 'src/User.model';
import { UserAuth } from 'src/UserAuth.model';
import { MusicuserService } from '../musicuser.service';



@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user=new UserAuth();
  isUserVisible=false
  istable=false;
  emailId:any;
  password:any;
  constructor(private userservice:MusicuserService, private router:Router) { }

  ngOnInit(): void {
  }

   saveUser(saveForm:NgForm){
    let user={"emailId":this.emailId,"password":this.password,"profilepic":""}
    console.log(this.emailId)
    console.log(this.password)
    let userFound:UserAuth;
    
    this.userservice.getUser(user).subscribe(
      data=>{
        userFound=data;
        if(userFound!=null){
            if(userFound.emailId==user.emailId && userFound.password==user.password){
            localStorage.emailId=user.emailId;
            localStorage.profilepic=userFound.profilepic;
              alert("Logged in!");
                this.router.navigate(['/home-page']);
            
                
            }
            else {
                alert("Invalid Email/Password!")
            }
        }
        else {
        alert("User Not Found!")
        }
      },
      error=>{
  console.log(error);
      }
    )
  console.log(localStorage.profilepic);
      
    }
}
