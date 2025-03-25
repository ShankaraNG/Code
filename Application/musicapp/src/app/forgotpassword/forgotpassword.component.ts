import { Component, OnInit } from '@angular/core';
import { ResetPassword } from 'src/ResetPassword.model';
import { MusicuserService } from '../musicuser.service';

@Component({
  selector: 'app-forgotpassword',
  templateUrl: './forgotpassword.component.html',
  styleUrls: ['./forgotpassword.component.css']
})
export class ForgotpasswordComponent implements OnInit {

  constructor(private musicuserservice:MusicuserService) { }

  ngOnInit(): void {
  }
  val=true;
  valu=true;
  arr:any;
  answer:any;
  emailId:any;
  password:any;
  confirmPassword:any;

  resetPassword()
   {
      let array=new ResetPassword();
      array.emailId=this.emailId;
     this.musicuserservice.resetpassword(array).subscribe(
       data=>{
       if(data!=null)
       {
        this.arr=data;
         if(this.answer==data.answer)
         {
           this.arr.password=this.password;
           this.arr.confirmPassword=this.confirmPassword;

           this.musicuserservice.changepass(this.arr).subscribe(
             data=>{console.log(data)},
             error=>{console.log(error)} 
           )
           alert("Password changed successfully!");
         }
         else{
           alert("Incorrect credentials");
         }
       }
       },
       error=>{console.log(error)}
     )
   }


}
