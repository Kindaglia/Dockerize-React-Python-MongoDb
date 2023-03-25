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
  newDocument: any = {};

  constructor(private http: HttpClient) {
    this.fetchDocuments();
  }

  fetchDocuments() {
    this.http.get<any[]>('http://localhost:5000/documento').subscribe((data) => {
      this.documents = data;
      console.log(data);
    });
  }

  addDocument() {
    this.http.post('http://localhost:5000/documento', this.newDocument).subscribe(() => {
      this.fetchDocuments();
      this.newDocument = {}; // reset the form
    });
  }

  deleteDocument(id: string) {
    this.http.delete(`http://localhost:5000/documento/${id}`).subscribe(() => {
      this.fetchDocuments();
    });
  }
}
