import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://localhost:5000';  // Cambia esta URL a la de tu servidor Flask

  constructor(private http: HttpClient) { }

  // Obtener departamentos
  getDepartamentos(): Observable<any> {
    return this.http.get(`${this.apiUrl}/listar_departamentos`);
  }

  // Crear un nuevo departamento
  createDepartamento(depto: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/crear_departamentos`, depto);
  }

  // Obtener gastos comunes
  getGastosComunes(): Observable<any> {
    return this.http.get(`${this.apiUrl}/gastos_comunes`);
  }

  // Crear gastos comunes
  createGastosComunes(gasto: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/crear_gastos_comunes`, gasto);
  }

  // Marcar un gasto común como pagado
  marcarComoPagado(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/marcar_como_pagado`, data);
  }

  // Listar gastos comunes pendientes
  listarGastosPendientes(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/listar_gastos_pendientes`, data);
  }
}
