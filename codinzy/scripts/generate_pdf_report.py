"""
PDF Report Generator for Codinzy Testing

This script generates comprehensive PDF reports for:
1. Automated Test Results
2. Manual Test Results
3. Combined Test Reports
4. Defect Reports

Requirements:
- reportlab
- jinja2
- matplotlib (for charts)
"""

import os
import sys
import json
import datetime
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from enum import Enum

# Add project paths
backend_path = Path(__file__).parent.parent.parent / 'backend'
sys.path.insert(0, str(backend_path))


class ReportType(Enum):
    AUTOMATED = "automated"
    MANUAL = "manual"
    COMBINED = "combined"
    DEFECT = "defect"


@dataclass
class TestResult:
    """Single test result"""
    test_id: str
    test_name: str
    module: str
    status: str  # PASS, FAIL, SKIP, BLOCK
    duration: float
    error_message: Optional[str] = None
    error_traceback: Optional[str] = None


@dataclass
class TestSuite:
    """Test suite results"""
    suite_name: str
    total_tests: int
    passed: int
    failed: int
    skipped: int
    blocked: int
    pass_rate: float
    duration: float
    tests: List[TestResult]
    coverage: Optional[Dict] = None


@dataclass
class CoverageData:
    """Code coverage data"""
    overall_coverage: float
    by_module: Dict[str, Dict]


@dataclass
class DefectInfo:
    """Defect information"""
    defect_id: str
    title: str
    module: str
    severity: str  # Critical, High, Medium, Low
    status: str
    reported_by: str
    reported_date: str
    description: str


class PDFReportGenerator:
    """Generate PDF reports for test results"""
    
    def __init__(self, output_dir: str = "testing/reports"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
    def generate_automated_test_report(
        self,
        test_suites: List[TestSuite],
        coverage_data: Optional[CoverageData],
        metadata: Dict
    ) -> str:
        """Generate automated test report PDF"""
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import (
            SimpleDocTemplate, Table, TableStyle, Paragraph,
            Spacer, Image, PageBreak, Flowable
        )
        from reportlab.graphics.shapes import Drawing
        from reportlab.graphics.widgets.grids import Grid, ShapedRect
        from reportlab.graphics.charts.piecharts import PieChart
        from reportlab.graphics.charts.barcharts import HorizontalBarChart
        
        # Create PDF
        filename = f"automated_test_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = self.output_dir / "pdf" / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        doc = SimpleDocTemplate(
            str(filepath),
            pagesize=A4,
            rightMargin=72,
            leftMargin=72,
            topMargin=72,
            bottomMargin=72
        )
        
        # Styles
        styles = getSampleStyleSheet()
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#1976D2')
        )
        
        heading_style = ParagraphStyle(
            'Heading',
            parent=styles['Heading2'],
            fontSize=16,
            spaceAfter=15,
            textColor=colors.HexColor('#333333')
        )
        
        normal_style = ParagraphStyle(
            'Normal',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=6
        )
        
        # Build story
        story = []
        
        # Title
        story.append(Paragraph(
            "Codinzy Automated Test Report",
            title_style
        ))
        story.append(Paragraph(
            f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}",
            normal_style
        ))
        story.append(Spacer(1, 20))
        
        # Executive Summary
        story.append(Paragraph("Executive Summary", heading_style))
        
        total_tests = sum(s.total_tests for s in test_suites)
        total_passed = sum(s.passed for s in test_suites)
        total_failed = sum(s.failed for s in test_suites)
        total_skipped = sum(s.skipped for s in test_suites)
        overall_pass_rate = (total_passed / total_tests * 100) if total_tests > 0 else 0
        
        summary_data = [
            ['Total Tests', str(total_tests)],
            ['Passed', str(total_passed)],
            ['Failed', str(total_failed)],
            ['Skipped', str(total_skipped)],
            ['Pass Rate', f"{overall_pass_rate:.1f}%"],
        ]
        
        summary_table = Table(summary_data, colWidths=[2*inch, 2*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
            ('TOPPADDING', (0, 0), (-1, -1), 12),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ]))
        story.append(summary_table)
        story.append(Spacer(1, 30))
        
        # Test Results by Suite
        story.append(Paragraph("Test Results by Module", heading_style))
        
        suite_data = [['Module', 'Total', 'Passed', 'Failed', 'Skipped', 'Pass Rate']]
        for suite in test_suites:
            suite_data.append([
                suite.suite_name,
                str(suite.total_tests),
                str(suite.passed),
                str(suite.failed),
                str(suite.skipped),
                f"{suite.pass_rate:.1f}%"
            ])
        
        suite_table = Table(suite_data, colWidths=[2*inch, inch, inch, inch, inch, inch])
        suite_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1976D2')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f5f5f5')]),
        ]))
        story.append(suite_table)
        story.append(Spacer(1, 30))
        
        # Coverage Section
        if coverage_data:
            story.append(Paragraph("Code Coverage Analysis", heading_style))
            
            coverage_data_list = [
                ['Module', 'Statements', 'Branches', 'Functions', 'Coverage']
            ]
            for module, coverage in coverage_data.by_module.items():
                coverage_data_list.append([
                    module,
                    str(coverage.get('statements', 0)),
                    str(coverage.get('branches', 0)),
                    str(coverage.get('functions', 0)),
                    f"{coverage.get('coverage', 0)}%"
                ])
            
            coverage_table = Table(coverage_data_list, colWidths=[1.5*inch, inch, inch, inch, inch])
            coverage_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#4CAF50')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ]))
            story.append(coverage_table)
            story.append(Spacer(1, 30))
        
        # Failed Tests
        all_failed_tests = []
        for suite in test_suites:
            for test in suite.tests:
                if test.status == 'FAIL':
                    all_failed_tests.append(test)
        
        if all_failed_tests:
            story.append(Paragraph("Failed Tests", heading_style))
            
            failed_data = [['Test ID', 'Test Name', 'Module', 'Error']]
            for test in all_failed_tests[:20]:  # Limit to 20
                error_short = test.error_message[:100] if test.error_message else 'N/A'
                failed_data.append([
                    test.test_id,
                    test.test_name[:30],
                    test.module,
                    error_short
                ])
            
            failed_table = Table(failed_data, colWidths=[1.2*inch, 2.5*inch, inch, 2*inch])
            failed_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f44336')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, -1), 9),
                ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
                ('TOPPADDING', (0, 0), (-1, -1), 6),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#c62828')),
            ]))
            story.append(failed_table)
        
        # Build PDF
        doc.build(story)
        return str(filepath)
    
    def generate_manual_test_report(
        self,
        test_cases: List[Dict],
        defects: List[DefectInfo],
        metadata: Dict
    ) -> str:
        """Generate manual test report PDF"""
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import (
            SimpleDocTemplate, Table, TableStyle, Paragraph,
            Spacer, PageBreak
        )
        
        filename = f"manual_test_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = self.output_dir / "pdf" / "manual" / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        doc = SimpleDocTemplate(str(filepath), pagesize=A4)
        styles = getSampleStyleSheet()
        
        story = []
        
        # Title
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#1976D2')
        )
        
        story.append(Paragraph("Codinzy Manual Test Report", title_style))
        story.append(Paragraph(
            f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}",
            styles['Normal']
        ))
        story.append(Spacer(1, 30))
        
        # Summary
        total = len(test_cases)
        passed = sum(1 for tc in test_cases if tc.get('status') == 'PASS')
        failed = sum(1 for tc in test_cases if tc.get('status') == 'FAIL')
        blocked = sum(1 for tc in test_cases if tc.get('status') == 'BLOCK')
        pass_rate = (passed / total * 100) if total > 0 else 0
        
        summary_data = [
            ['Total Test Cases', str(total)],
            ['Executed', str(passed + failed + blocked)],
            ['Passed', str(passed)],
            ['Failed', str(failed)],
            ['Blocked', str(blocked)],
            ['Not Tested', str(total - (passed + failed + blocked))],
            ['Pass Rate', f"{pass_rate:.1f}%"],
        ]
        
        summary_table = Table(summary_data, colWidths=[2*inch, 2*inch])
        summary_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('FONTSIZE', 12),
            ('BOTTOMPADDING', 12),
        ]))
        story.append(summary_table)
        story.append(Spacer(1, 30))
        
        # Test Results by Module
        modules = {}
        for tc in test_cases:
            module = tc.get('module', 'Other')
            if module not in modules:
                modules[module] = {'total': 0, 'passed': 0, 'failed': 0}
            modules[module]['total'] += 1
            if tc.get('status') == 'PASS':
                modules[module]['passed'] += 1
            elif tc.get('status') == 'FAIL':
                modules[module]['failed'] += 1
        
        module_data = [['Module', 'Total', 'Passed', 'Failed', 'Pass Rate']]
        for module, data in modules.items():
            rate = (data['passed'] / data['total'] * 100) if data['total'] > 0 else 0
            module_data.append([
                module,
                str(data['total']),
                str(data['passed']),
                str(data['failed']),
                f"{rate:.1f}%"
            ])
        
        module_table = Table(module_data, colWidths=[2*inch, inch, inch, inch, inch])
        module_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1976D2')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ]))
        story.append(Paragraph("Test Results by Module", styles['Heading2']))
        story.append(module_table)
        story.append(Spacer(1, 30))
        
        # Defects Summary
        if defects:
            story.append(Paragraph("Defects Summary", styles['Heading2']))
            
            defect_data = [['ID', 'Title', 'Module', 'Severity', 'Status']]
            for d in defects:
                defect_data.append([
                    d.defect_id,
                    d.title[:40],
                    d.module,
                    d.severity,
                    d.status
                ])
            
            defect_table = Table(defect_data, colWidths=[1*inch, 2.5*inch, inch, inch, inch])
            defect_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f44336')),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.grey),
                ('FONTSIZE', 9),
            ]))
            story.append(defect_table)
        
        doc.build(story)
        return str(filepath)
    
    def generate_defect_report(
        self,
        defects: List[DefectInfo],
        metadata: Dict
    ) -> str:
        """Generate defect report PDF"""
        from reportlab.lib import colors
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
        
        filename = f"defect_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        filepath = self.output_dir / "pdf" / "defects" / filename
        filepath.parent.mkdir(parents=True, exist_ok=True)
        
        doc = SimpleDocTemplate(str(filepath), pagesize=A4)
        styles = getSampleStyleSheet()
        story = []
        
        # Title
        story.append(Paragraph("Codinzy Defect Report", styles['Heading1']))
        story.append(Spacer(1, 20))
        
        # Summary by Severity
        severity_counts = {'Critical': 0, 'High': 0, 'Medium': 0, 'Low': 0}
        status_counts = {'New': 0, 'Open': 0, 'In Progress': 0, 'Resolved': 0, 'Closed': 0}
        
        for d in defects:
            if d.severity in severity_counts:
                severity_counts[d.severity] += 1
            if d.status in status_counts:
                status_counts[d.status] += 1
        
        # Defect List
        defect_data = [['ID', 'Title', 'Module', 'Severity', 'Status', 'Reported By']]
        for d in defects:
            defect_data.append([
                d.defect_id,
                d.title[:35],
                d.module,
                d.severity,
                d.status,
                d.reported_by[:15]
            ])
        
        table = Table(defect_data, colWidths=[0.8*inch, 2.5*inch, inch, 0.8*inch, 1*inch, 1*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#c62828')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.grey),
            ('FONTSIZE', 9),
        ]))
        story.append(table)
        
        doc.build(story)
        return str(filepath)


def run_report_generation():
    """Main function to generate all reports"""
    import json
    
    generator = PDFReportGenerator()
    
    # Load test results from JSON files
    automated_results_file = Path("testing/reports/automated/json/backend_results.json")
    manual_results_file = Path("testing/reports/manual/json/test_results.json")
    
    if automated_results_file.exists():
        with open(automated_results_file) as f:
            results = json.load(f)
            
            # Create test suites from results
            test_suites = []
            for suite_data in results.get('test_results', {}).values():
                suite = TestSuite(
                    suite_name=suite_data.get('module', 'Unknown'),
                    total_tests=suite_data.get('total', 0),
                    passed=suite_data.get('passed', 0),
                    failed=suite_data.get('failed', 0),
                    skipped=0,
                    blocked=0,
                    pass_rate=suite_data.get('pass_rate', 0),
                    duration=0,
                    tests=[]
                )
                test_suites.append(suite)
            
            coverage_data = CoverageData(
                overall_coverage=results.get('coverage', {}).get('overall', {}).get('coverage_percentage', 0),
                by_module=results.get('coverage', {}).get('by_module', {})
            )
            
            # Generate report
            filepath = generator.generate_automated_test_report(
                test_suites,
                coverage_data,
                results.get('report_metadata', {})
            )
            print(f"Generated automated test report: {filepath}")
    
    print("Report generation completed.")


if __name__ == "__main__":
    run_report_generation()
