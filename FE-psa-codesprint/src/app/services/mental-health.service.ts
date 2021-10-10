import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { EmployeeData } from '../models/employee-data';
import { EmployeeRating } from '../models/employee-rating';

const baseUrl = 'http://localhost:8080';
const replUrl = 'http://codesprint.brandoncjh.repl.co'; 

export interface GetAllUsersResponse {
  result: EmployeeRating[],
  allEmployeeData: EmployeeData[]
}

export interface GetScoreAndInfoByName {
  employeeData: EmployeeData,
  employeeScore: EmployeeRating
}

@Injectable({
  providedIn: 'root'
})
export class MentalHealthService {

  constructor(private http: HttpClient) {}

  getAllUsers(): Observable<GetAllUsersResponse> {
    console.log('calling getAllUsers()');
    return this.http.get<GetAllUsersResponse>(replUrl + '/getrating');
  }

  getScoreAndInfoByName(name: string): Observable<GetScoreAndInfoByName> {
    return this.http.get<GetScoreAndInfoByName>(replUrl + '/getscorebyname?name=' + name);
  }

}
