import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,

    FormsModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule // Aggiungi questa riga
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
