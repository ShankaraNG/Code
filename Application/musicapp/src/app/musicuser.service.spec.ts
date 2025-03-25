import { TestBed } from '@angular/core/testing';

import { MusicuserService } from './musicuser.service';

describe('MusicuserService', () => {
  let service: MusicuserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(MusicuserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
