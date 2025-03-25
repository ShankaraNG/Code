import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})
export class LogoutComponent implements OnInit {
  emailId: any;

  constructor(private router:Router) { }

  ngOnInit(): void {
    this.logout();
  }

  logout()
  {
    this.emailId=localStorage.emailId;
    if( this.emailId.length!=0)
    {
      localStorage.emailId="";
      localStorage.profilepic="";
      alert('logged out');
      this.router.navigate(['/login']);
    
    }
    else
    {
      alert('login first');
      this.router.navigate(['/login']);
    }
    console.log(localStorage.emailId);

  }
}
