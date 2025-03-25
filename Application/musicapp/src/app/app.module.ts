import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { registerComponent } from './register/register.component';
import { LoginComponent } from './login/login.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { HomePageComponent } from './home-page/home-page.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import { ForgotpasswordComponent } from './forgotpassword/forgotpassword.component';
import { RecommendedComponent } from './recommended/recommended.component';
import { FavouriteComponent } from './favourite/favourite.component';
import { LogoutComponent } from './logout/logout.component';
import { DeleteComponent } from './delete/delete.component';
import { AccountComponent } from './account/account.component';



@NgModule({
  declarations: [
    AppComponent,
    registerComponent,
    LoginComponent,
    HomePageComponent,
    ForgotpasswordComponent,
    RecommendedComponent,
    FavouriteComponent,
    LogoutComponent,
    DeleteComponent,
    AccountComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    MatToolbarModule,
    MatButtonModule

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
