import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { EmployeeData } from '../models/employee-data';
import { EmployeeRating } from '../models/employee-rating';

const baseUrl = 'http://localhost:8080';

export interface GetAllUsersResponse {
  allEmployeeData: EmployeeData[],
  allEmployeeScore: EmployeeRating[]
}

@Injectable({
  providedIn: 'root'
})
export class MentalHealthService {

  constructor(private http: HttpClient) {}

  getAllUsers(): Observable<GetAllUsersResponse> {
    console.log('calling getAllUsers()');
    return this.http.get<GetAllUsersResponse>(baseUrl + '/getallscore');
  }

}
