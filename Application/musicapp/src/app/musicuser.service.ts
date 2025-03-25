import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { User } from 'src/User.model';
import { UserAuth } from 'src/UserAuth.model';
import { ResetPassword } from 'src/ResetPassword.model';
import { Album } from 'src/Album.model';
import { favourite } from 'src/favourite.model';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class MusicuserService {

  constructor(private http: HttpClient) { }

  saveUser(User: User) {

    return this.http.post<User>('http://localhost:3331/user', User);
  }
  getUser(userAuth: UserAuth) {

    return this.http.post<UserAuth>(`http://localhost:3331/user/login`, userAuth);
  }
  resetpassword(emailId: ResetPassword) {
    return this.http.post<User>("http://localhost:3331/user/reset", emailId);
  }
  changepass(User: User) {
    return this.http.put<User>("http://localhost:3331/user/register", User);
  }
  deleteUser(emailId: string, password: string) {

    return this.http.delete<User>(`http://localhost:3331/user/delete/${emailId}/${password}`);

  }
  gettopTracks() {

    return this.http.get('https://api.napster.com/v2.1/tracks/top?apikey=ZTk2YjY4MjMtMDAzYy00MTg4LWE2MjYtZDIzNjJmMmM0YTdm');

  }

  savetracks(data: Album) {
    return this.http.post<Album>("http://localhost:3331/user/savealbum", data);
  }

  addToFavourite(data: favourite) {
    return this.http.post<favourite>("http://localhost:3331/fav/addfav", data);
  }

  getFavourite(data: string) {
    return this.http.get<favourite[]>(`http://localhost:3331/fav/getfav/${data}`);
  }

  deleteFavourite(emailId: string, albumName: string) {

    return this.http.delete<favourite>(`http://localhost:3331/fav/deletefav/${emailId}/${albumName}`)

  }

  getaccount(emailId: string): Observable<User> {

    return this.http.get<User>(`http://localhost:3331/user/getUser/${emailId}`);

  }


  // gettracks()
  // {
  //   return this.http.get<Album>("http://localhost:3331/user/get");
  // }
  // gettracks(emailId:string)
  // {

  //  return this.http.get<Albumn>(`http://localhost:3331/user/${emailId}`)

  // }

  // deletetracks(obj:any)
  // {
  //   return this.http.delete<Album>(`http://localhost:3331/user/delete/${obj}`);
  // }
}
