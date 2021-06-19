package cse360assign3;

import static org.junit.Assert.*;

import org.junit.Test;

public class CalculatorTest {

	@Test
	public void testCalculator() {
		Calculator cal = new Calculator();
		assertEquals(cal.getTotal(), 0);
	}
	
	@Test
	public void testGetTotal() {
		Calculator cal = new Calculator();
		
	}

	@Test
	public void testAdd() {
		Calculator cal = new Calculator();
		cal.add(5);
		assertEquals(cal.getTotal(), 5);
	}
	
	@Test
	public void testSubtract() {
		Calculator cal = new Calculator();
		cal.add(5);
		cal.subtract(3);
		assertEquals(cal.getTotal(), 2);
	}
	
	@Test
	public void testMultiply() {
		Calculator cal = new Calculator();
		cal.add(5);
		cal.subtract(3);
		cal.multiply(3);
		assertEquals(cal.getTotal(), 6);
	}
	
	@Test
	public void testDivide() {
		Calculator cal = new Calculator();
		cal.add(5);
		cal.subtract(3);
		cal.multiply(3);
		cal.divide(2);
		assertEquals(cal.getTotal(), 3);
		cal.divide(0);
		assertEquals(cal.getTotal(), 0);
	}
	
	@Test
	public void testGetHistory() {
		Calculator cal = new Calculator();
		cal.add(4);
		cal.subtract(2);
		cal.multiply(2);
		cal.add(5);
		assertEquals(cal.getHistory(), "0 + 4 - 2 * 2 + 5");
	}

}
