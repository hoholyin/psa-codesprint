import { Component, OnInit } from '@angular/core';
import { User } from 'src/app/models/user';
import { MentalHealthService } from 'src/app/services/mental-health.service';

@Component({
  selector: 'app-overview-page',
  templateUrl: './overview-page.component.html',
  styleUrls: ['./overview-page.component.scss']
})
export class OverviewPageComponent implements OnInit {

  dataSource: User[] = [
    {name: 'Glenn Tan', score: 50},
    {name: 'Hol Yin', score: 80},
    {name: 'Brandon', score: 90}
  ];

  displayedColumns = ['name', 'score'];

  constructor(private mentalHealthSerivce: MentalHealthService) { }

  ngOnInit(): void {
  }

}
