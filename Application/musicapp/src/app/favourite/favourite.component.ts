import { Component, OnInit } from '@angular/core';
import { MusicuserService } from '../musicuser.service';
import { favourite } from 'src/favourite.model';

@Component({
  selector: 'app-favourite',
  templateUrl: './favourite.component.html',
  styleUrls: ['./favourite.component.css']
})
export class FavouriteComponent implements OnInit {

  constructor(private http: MusicuserService) { }

  ngOnInit(): void {
    this.gettracks()
  }
  albums: any = [];
  favourites: favourite[] = [];
  gettracks() {
    //get email from localstorage;
    // localStorage.emailId="abcd@gmail.com";
    let emailId = localStorage.emailId;

    this.http.getFavourite(emailId).subscribe(
      data => {
        this.favourites = data;
        console.log(data);
      },
      error => console.log(error)

    )

  }

  deletedata(name: any) {
    let emailId = localStorage.emailId;
    this.http.deleteFavourite(emailId, name).subscribe(
      data => {
        this.gettracks();
        console.log(data)
      },
      error => { console.log(error) }
    )
  }

}
