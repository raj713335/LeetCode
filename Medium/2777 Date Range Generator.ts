# https://leetcode.com/problems/date-range-generator/description/

function* dateRangeGenerator(start: string, end: string, step: number) : Generator<string> {

    while (new Date(start).valueOf() <= new Date(end).valueOf()) {
        yield start;
        const nextDate = rangeGenerator(start, step);
        start = nextDate;
    }
    
};

function rangeGenerator(start: string, step: number): string {

    return new Date(new Date(start).valueOf() + step * 86400000).toISOString().split("T")[0]

}

/**
 * const g = dateRangeGenerator('2023-04-01', '2023-04-04', 1);
 * g.next().value; // '2023-04-01'
 * g.next().value; // '2023-04-02'
 * g.next().value; // '2023-04-03'
 * g.next().value; // '2023-04-04'
 * g.next().done; // true
 */
