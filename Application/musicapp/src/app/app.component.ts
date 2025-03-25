import { Component } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'muzix';

  pic: any;
  ngOnInit() {

    if (localStorage.profilepic.length != 0) {
      this.pic = localStorage.profilepic;
    }
    else {
      this.pic = "../assets/profile/blank.png";
    }
  }
}
