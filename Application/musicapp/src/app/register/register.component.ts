import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { User } from 'src/User.model';
import { MusicuserService } from '../musicuser.service';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class registerComponent {
  user = new User();
  constructor(private userservice: MusicuserService) { }

  myimg:any;

onFileSelected(fileInput:any)
{
  if(fileInput.target.files && fileInput.target.files[0])
  {

    let rdr= new FileReader();
    rdr.onload = (e:any)=>{
      let img= new Image();
      img.src=e.target.result;
      img.onload= rs=>{
       this.myimg= e.target.result;
      }
    };
    rdr.readAsDataURL(fileInput.target.files[0]);
  }


}

  saveUser(saveForm: NgForm) {
    this.user.profilepic=this.myimg;
    this.userservice.saveUser(this.user).subscribe(
      (data: User) => {
        this.user = data;
        console.log('data ' + this.user);
      },
      (error: string) => {
        console.log('error ' + error)
      }
    )
  }
}