import { favourite } from 'src/favourite.model';
import { Album } from 'src/Album.model';
import { Component, OnInit } from '@angular/core';
import { MusicuserService } from '../musicuser.service';



@Component({
  selector: 'app-recommended',
  templateUrl: './recommended.component.html',
  styleUrls: ['./recommended.component.css']
})
export class RecommendedComponent implements OnInit {
  imgart: string[] = ['../assets/Images/1.jpg', '../assets/Images/2.jpg', '../assets/Images/3.jpg', '../assets/Images/4.jpg', '../assets/Images/5.jpg', '../assets/Images/6.jpg', '../assets/Images/7.jpg', '../assets/Images/8.jpg', '../assets/Images/9.jpg', '../assets/Images/10.jpg'];

  constructor(private http: MusicuserService) { }

  ngOnInit(): void {
    this.getTopTracks();
  }

  albums: Album[] = [];
  getTopTracks() {

    this.http.gettopTracks().subscribe(
      data => {

        let myjosn = JSON.parse(JSON.stringify(data));

        console.log(myjosn.tracks);

        for (let i = 0; i < myjosn.tracks.length; i++) {
          //console.log(myjosn.tracks[i].albumName);
          // this.albums[i].albumName=myjosn.tracks[i].albumName;
          // this.albums[i].artistName=myjosn.tracks[i].artistName;
          // this.albums[i].name=myjosn.tracks[i].links.name;
          // this.albums[i].previewUrl=myjosn.tracks[i].links.previewUrl;
          let myAlbum = new Album();
          myAlbum.albumName = myjosn.tracks[i].albumName;
          myAlbum.artistName = myjosn.tracks[i].artistName;
          myAlbum.name = myjosn.tracks[i].links.name;
          myAlbum.previewUrl = myjosn.tracks[i].previewURL;
          myAlbum.imgurl = this.imgart[i];
          this.albums.push(myAlbum);
        }

      }
      ,
      error => {
        console.log(error)
      }
    )


  }
  emailId: any;
  savedata(obj: any) {
    this.emailId = localStorage.emailId;
    if (this.emailId == 0) {
      alert('login first to add musics to your favourites');
    }
    else {
      let myFav = new favourite();
      myFav.emailId = this.emailId;
      myFav.albumName = obj.albumName;
      myFav.artistName = obj.artistName;
      myFav.name = obj.name;
      myFav.previewUrl = obj.previewUrl;
      myFav.imgurl = obj.imgurl;

      this.http.addToFavourite(myFav).subscribe(
        data => { console.log(data) },
        error => { console.log(error) }
      )
    }
  }
}
