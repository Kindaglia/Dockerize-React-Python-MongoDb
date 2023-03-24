import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'Frontend';
  documents: any[] = [];

  constructor(private http: HttpClient) {
    this.http.get<any[]>('http://localhost:5000/documento').subscribe((data) => {
      this.documents = data;
      console.log(data);
    });
  }
}
