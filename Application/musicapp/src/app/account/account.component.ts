import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from 'src/User.model';
import { MusicuserService } from '../musicuser.service';

@Component({
  selector: 'app-account',
  templateUrl: './account.component.html',
  styleUrls: ['./account.component.css']
})
export class AccountComponent implements OnInit {
  profilepic: any;

  constructor(private http: MusicuserService, private router: Router) { }

  ngOnInit(): void {
    this.getaccount();
    // this.myimg=localStorage.profilepic;
  }
  user = new User();
  emailId: any;
  // myimg:any;
  getaccount() {
    let emailId = localStorage.emailId;
    // this.profilepic=localStorage.profilepic;
    if (this.emailId == 0) {
      alert('login first');
      this.router.navigate(['/login']);

    }
    else {
      this.http.getaccount(emailId).subscribe(
        data => {
          this.user = data;
          console.log(data);
        },
        error => alert(error)
      )
    }

  }
}
