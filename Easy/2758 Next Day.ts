# https://leetcode.com/problems/next-day/description/

declare global {
    interface Date {
        nextDay(): string;
    }
}

Date.prototype.nextDay = function(): string {
	const tomorrow = new Date(this);

    tomorrow.setDate(tomorrow.getDate() + 1);

    return tomorrow.toISOString().split('T')[0];
}

/**
 * const date = new Date("2014-06-20");
 * date.nextDay(); // "2014-06-21"
 */
