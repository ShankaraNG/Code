import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { User } from 'src/User.model';
import { MusicuserService } from '../musicuser.service';

@Component({
  selector: 'app-delete',
  templateUrl: './delete.component.html',
  styleUrls: ['./delete.component.css']
})
export class DeleteComponent implements OnInit {

  constructor(private http:MusicuserService, private router:Router) { }

  user=new User();
  isUserVisible=false
  istable=false;
  emailId:any;
  password:any;
  ngOnInit(): void {
  }

  deleteUser(saveForm:NgForm){
    let user={"emailId":this.emailId, "password":this.password}
    console.log(this.emailId);
    console.log(this.password);
    let userFound:User;
    this.http.deleteUser(this.emailId, this.password).subscribe(
      data=>{
        userFound=data;
        if(userFound!=null){
            if(userFound.emailId==user.emailId, userFound.password==user.password){
              console.log(data);
              alert("account deleted");
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
}
}
