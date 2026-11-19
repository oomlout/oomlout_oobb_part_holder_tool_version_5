$fn = 50;

difference() {
	union() {
		translate(v = [0, 0, -33.0]) {
			hull() {
				translate(v = [-47.0, 69.5, 0]) {
					cylinder(h = 66, r = 5);
				}
				translate(v = [47.0, 69.5, 0]) {
					cylinder(h = 66, r = 5);
				}
				translate(v = [-47.0, -69.5, 0]) {
					cylinder(h = 66, r = 5);
				}
				translate(v = [47.0, -69.5, 0]) {
					cylinder(h = 66, r = 5);
				}
			}
		}
	}
	union() {
		translate(v = [-45.0, -67.5, -34.0]) {
			cylinder(h = 68, r = 3.25);
		}
		translate(v = [-45.0, 67.5, -34.0]) {
			cylinder(h = 68, r = 3.25);
		}
		translate(v = [45.0, -67.5, -34.0]) {
			cylinder(h = 68, r = 3.25);
		}
		translate(v = [45.0, 67.5, -34.0]) {
			cylinder(h = 68, r = 3.25);
		}
		translate(v = [0.0, -47, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 11) {
					polygon(points = [[-11.5, -30], [-11.5, 5], [-33, 30], [-42, 80], [42, 80], [33, 30], [11.5, 5], [11.5, -30]]);
				}
			}
		}
		translate(v = [0.0, -32.5, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 10) {
					polygon(points = [[-17, -30], [-17, 24], [-46, 63], [-50, 95], [50, 95], [46, 63], [17, 24], [17, -30]]);
				}
			}
		}
		translate(v = [0.0, -17, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 11) {
					polygon(points = [[-17, -30], [-17, 5], [-45, 50], [-55, 90], [55, 90], [45, 50], [17, 5], [17, -30]]);
				}
			}
		}
		translate(v = [-37.5, 0, -30]) {
			cylinder(h = 60, r = 1.75);
		}
		translate(v = [-37.5, 0, 30]) {
			cylinder(h = 98, r = 9);
		}
		translate(v = [-15.0, 0, -30]) {
			cylinder(h = 60, r = 1.75);
		}
		translate(v = [-15.0, 0, 30]) {
			cylinder(h = 98, r = 9);
		}
		translate(v = [7.5, 0, -30]) {
			cylinder(h = 60, r = 2.5);
		}
		translate(v = [7.5, 0, 30]) {
			cylinder(h = 98, r = 9);
		}
		translate(v = [-30.0, 37.5, -30]) {
			cylinder(h = 57, r = 3.85);
		}
		translate(v = [-30.0, 37.5, 27]) {
			cylinder(h = 30, r = 5.5);
		}
		translate(v = [-30.0, 37.5, 57]) {
			cylinder(h = 17, r = 6.5);
		}
		translate(v = [-30.0, 37.5, 74]) {
			cylinder(h = 100, r = 18);
		}
		translate(v = [0.0, 2.25, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 4.5) {
					polygon(points = [[22, -30], [22, 80], [38, 80], [38, -30]]);
				}
			}
		}
		translate(v = [0.0, 17.75, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 5.5) {
					polygon(points = [[21, -30], [21, 90], [39, 90], [39, -30]]);
				}
			}
		}
		translate(v = [0.0, 33.5, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 7) {
					polygon(points = [[18.5, -30], [18.5, 110], [41.5, 110], [41.5, -30]]);
				}
			}
		}
		translate(v = [0.0, 48.5, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 7) {
					polygon(points = [[18.5, -30], [18.5, 110], [41.5, 110], [41.5, -30]]);
				}
			}
		}
		translate(v = [0.0, 51.25, 0]) {
			rotate(a = [90, 0, 0]) {
				linear_extrude(height = 27.5) {
					polygon(points = [[-8.5, -30], [-8.5, 130], [8.5, 130], [8.5, -30]]);
				}
			}
		}
		translate(v = [-32.5, -67.5, -7]) {
			cylinder(h = 100, r = 1.55);
		}
		translate(v = [-27.5, -67.5, -12]) {
			cylinder(h = 100, r = 1.8);
		}
		translate(v = [-22.5, -67.5, -17]) {
			cylinder(h = 100, r = 1.95);
		}
		translate(v = [-17.5, -67.5, -22]) {
			cylinder(h = 100, r = 2.25);
		}
		translate(v = [-12.5, -67.5, -27]) {
			cylinder(h = 100, r = 2.75);
		}
		translate(v = [30.0, 60, -30]) {
			cylinder(h = 137, r = 6.5);
		}
	}
}
